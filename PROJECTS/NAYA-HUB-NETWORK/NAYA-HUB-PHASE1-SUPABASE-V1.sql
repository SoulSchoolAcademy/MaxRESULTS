-- Naya Hub Phase 1 durable boundary
-- Authority: Supabase Auth + database for member state and immutable historical results.
-- MAXESS remains the scoring/result authority. This schema stores, validates, and retrieves; it does not rescore.

create extension if not exists pgcrypto;

create table if not exists public.members (
  id uuid primary key references auth.users(id) on delete cascade,
  display_name text not null default '',
  email text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.assessment_results (
  result_id uuid primary key default gen_random_uuid(),
  member_id uuid not null references public.members(id) on delete cascade,
  assessment_id text not null,
  assessment_version text not null,
  score integer not null check (score between 0 and 100),
  mastery_band text not null,
  dimension_results jsonb not null,
  fingerprint jsonb,
  result_payload jsonb not null,
  created_at timestamptz not null default now(),
  constraint assessment_results_payload_contract check (
    result_payload->>'contractVersion' = 'MAXESS_RESULT_V1'
  ),
  constraint assessment_results_payload_score check (
    (result_payload->>'overallScore')::integer = score
  )
);

create index if not exists assessment_results_member_created_idx
  on public.assessment_results(member_id, created_at desc);

create index if not exists assessment_results_assessment_idx
  on public.assessment_results(assessment_id, assessment_version);

-- Member profile is updated only through the authenticated application boundary.
create or replace function public.touch_members_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

drop trigger if exists members_touch_updated_at on public.members;
create trigger members_touch_updated_at
before update on public.members
for each row execute function public.touch_members_updated_at();

-- Historical results are immutable. Versioned repair/migration must happen through a controlled service path.
create or replace function public.reject_result_mutation()
returns trigger
language plpgsql
as $$
begin
  raise exception 'Historical MAXESS results are immutable';
end;
$$;

drop trigger if exists assessment_results_immutable_update on public.assessment_results;
create trigger assessment_results_immutable_update
before update or delete on public.assessment_results
for each row execute function public.reject_result_mutation();

alter table public.members enable row level security;
alter table public.assessment_results enable row level security;

-- Members may read their own identity. Writes are performed by the authenticated application boundary.
drop policy if exists members_select_self on public.members;
create policy members_select_self
on public.members for select
to authenticated
using (id = auth.uid());

-- Members may read their own historical results. Direct client inserts/updates/deletes are intentionally denied.
drop policy if exists results_select_self on public.assessment_results;
create policy results_select_self
on public.assessment_results for select
to authenticated
using (member_id = auth.uid());

-- No direct INSERT/UPDATE/DELETE policies are created for authenticated clients.
-- The secure Vercel/API boundary must:
--   1. authenticate the member;
--   2. validate MAXESS_RESULT_V1 against the canonical contract;
--   3. verify member ownership;
--   4. insert exactly one historical record;
--   5. never recompute historical scores;
--   6. use the server-side Supabase service role only after those checks.

comment on table public.members is 'Canonical Naya member identity boundary; id is the stable member ID and equals the authenticated Supabase user ID.';
comment on table public.assessment_results is 'Immutable historical MAXESS_RESULT_V1 records. MAXESS owns scoring semantics; this table owns durable historical truth.';
