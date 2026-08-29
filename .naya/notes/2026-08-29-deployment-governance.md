# Naya Note — Deployment Governance

## Discovery
A repository change was unexpectedly being treated as a Vercel deployment event. This exposed a dangerous coupling: source-of-truth activity was being conflated with publication.

## Learning
**CONNECTED ≠ DEPLOYABLE. COMMITTED ≠ RELEASED.**

Repository activity is primarily knowledge, governance, implementation, testing, or research work. Deployment is a privileged side effect and must be independently authorized.

## Canonical Rule
NayaPOWER defaults all Vercel deployment to DENY. The only permitted deployment path is `.github/workflows/authorized-vercel-release.yml`, which requires:

1. explicit manual release invocation;
2. exact commit SHA checkout and verification;
3. successful deployment-governance verification;
4. a complete machine-readable release authorization;
5. explicit approval;
6. exact target environment binding;
7. exact canonical Vercel project binding; and
8. Vercel credentials before the deployment command can execute.

## Value
This prevents documentation, Smart Notes, governance changes, experiments, ordinary commits, and other repository activity from consuming deployment resources or accidentally changing live state.

## Compounding Lesson
**Publication should be a deliberate consequence of verified value, never an accidental consequence of activity.**

## Verification State
Repository implementation is present. Provider-side deployment success of the new authorized workflow remains UNKNOWN until that workflow is intentionally exercised with valid Vercel credentials and an authorized commit.
