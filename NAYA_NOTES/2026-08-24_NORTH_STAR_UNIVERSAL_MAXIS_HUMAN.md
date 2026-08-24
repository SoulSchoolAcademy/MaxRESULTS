# SHAWN / HUMAN NOTE — THE NEW NORTH STAR

**Date:** August 24, 2026  
**For:** Shawn and anyone who needs to understand the idea later  
**Canonical name:** Shawn — S-H-A-W-N

# The Big Idea

We are not just building an AI scorecard.

We are building a way for a person to say:

> **“This is what I want to learn.”**

…and immediately get a personalized assessment of where they are.

Then, with Naya Power, they can actually learn the subject, practice it, remember it, improve, take the test again, and watch themselves grow.

That is the bigger product.

MAXIS is the engine that measures the journey.

---

# What the Person Will See

The front of the app should be wonderfully simple.

### 1. Enter your name

### 2. Enter the subject or topic you want to be assessed on

They can type it or, eventually, speak it.

Something like:

> **What would you like to be assessed on?**
>
> *The more specific you are, the more accurately we can create your assessment.*
>
> **Type or speak your topic.**

Then:

# **START MY FREE ASSESSMENT**

The promise is simple:

> **Free 3-minute assessment. Immediate results. See your score and get personalized feedback on where you are today.**

The person's name makes the report feel like it belongs to them:

> **Shawn — Artificial Intelligence**
>
> **Your Score: 82**
>
> **Level: Advancing**

---

# Why This Is Powerful

The person doesn't have to know what course to buy.

They don't have to search through hundreds of subjects.

They don't have to know the perfect curriculum.

They simply say what they want to know.

It could be:

- Algebra
- French
- Biology
- Guitar
- Coding
- History
- Marketing
- Physics
- Psychology
- Photography
- Artificial intelligence
- Anything else that can be meaningfully assessed

The system figures out how to turn the topic into an assessment.

That's the important change.

---

# MAXIS Becomes the Universal Assessment Engine

Right now, MAXIS is essentially built around a particular assessment.

The new goal is different.

We don't want to build:

> MAXIS Biology
>
> MAXIS French
>
> MAXIS Coding
>
> MAXIS History

We want:

> **MAXIS — the engine that can assess many subjects.**

The subject changes.

The engine doesn't.

The questions change.

The scoring system remains consistent.

That means we build the engine once and let the intelligence layer create the assessment for the subject.

---

# The Simple Picture

```text
PERSON
  ↓
“I want to be assessed on photography.”
  ↓
NAYA understands the topic
  ↓
NAYA creates the assessment
  ↓
MAXIS gives the test
  ↓
PERSON answers
  ↓
MAXIS scores it
  ↓
PERSON gets a personalized report
  ↓
NAYA says:
“Now imagine if I helped you improve that score.”
```

That is the bridge between MAXIS and Naya Power.

---

# And Then It Gets Much Bigger

The free test is only the beginning.

Imagine this:

```text
LEARN
 ↓
PRACTICE
 ↓
TAKE TEST
 ↓
GET SCORE
 ↓
SEE WHAT TO IMPROVE
 ↓
LEARN MORE
 ↓
TAKE TEST AGAIN
 ↓
GET BETTER SCORE
 ↓
MASTER IT
```

And then you can do it again with another subject.

And another.

And another.

That's the idea behind **CISS — Compounding Intelligence System**.

Your learning doesn't have to disappear after the course ends.

It can keep building.

---

# The Score Isn't a Judgment

This is important.

If someone gets 42%, that isn't:

> “You're bad at this.”

It's:

> “Here's where you are today.”

Then they learn.

Maybe the next score is 63%.

Then 78%.

Then 91%.

Now the score becomes a record of growth.

### Emerging → Foundation → Developing → Advancing → Mastering

The user can keep trying.

The system is there to help them improve, not embarrass them.

---

# Naya Is the Teacher

This is where Naya Power becomes much more than a quiz website.

Imagine having a master teacher beside you whenever you need one.

You say:

> “Naya, teach me physics.”

She can explain it.

You ask questions.

She explains it another way.

You get stuck.

She helps.

You want examples.

She gives examples.

You want to build something with what you learned.

She helps you build it.

You want to test yourself.

MAXIS tests you.

You want to know what you forgot six months later.

You ask Naya.

That's the relationship we're trying to create.

---

# Naya Should Have a Voice

The current system already has a Naya/listen experience and visual speaking states.

The strategic goal is to go beyond the generic robotic browser “read aloud” feature.

Instead:

```text
Naya creates the words
      ↓
Naya voice system
      ↓
Naya actually speaks
```

That means the experience can eventually feel like **Naya is talking to you**, rather than a computer reading text.

That's an important part of making Naya feel like a real learning companion.

---

# Certificates and Recognition

Eventually, when someone has actually demonstrated knowledge, MAXIS can become the gatekeeper for an achievement.

For example:

> **Naya Power Academy**
>
> Certificate of Excellence
>
> Shawn Vibert
>
> Artificial Intelligence
>
> Score: 93%
>
> Level: Mastering
>
> Certificate ID: NP-XXXX

We can add a QR code or verification system so someone can verify that the achievement came from the system.

The certificate isn't the important part.

The **real learning is the important part.**

The certificate is recognition of it.

---

# The Free Assessment Is the Front Door

This makes the free assessment strategically powerful.

Someone comes because they're curious:

> **“How good am I at this?”**

They get something useful immediately.

Then they see:

> **“Here's where you are.”**

And Naya can naturally say:

> **“Want to improve it?”**

That's where Naya Power comes in.

So the assessment isn't just a scorecard.

It's the doorway into the larger experience.

---

# What We Already Have

We should not throw MAXIS away.

The current E00 118 implementation already gives us a substantial foundation:

- premium visual assessment shell
- progress indicator
- Naya interaction
- question display
- answer cards
- selected-answer states
- Continue flow
- responsive behavior
- dialogs
- results area

The E00 bridge/controller pieces also show that we've already started separating the assessment from the results release process.

That is good architecture to build upon.

---

# The Current Technical Problem

Before we make MAXIS universal, we have to make sure the current score actually works reliably.

We need to trace:

```text
Answer selected
 ↓
Answer saved
 ↓
Question identified
 ↓
Dimension identified
 ↓
Score retrieved
 ↓
Weights applied
 ↓
Dimensions calculated
 ↓
Overall score calculated
 ↓
Mastery level determined
 ↓
Official result created
 ↓
Results released
```

We should find the actual break in that chain instead of guessing.

Once that works perfectly, we generalize it.

---

# The Bigger Architecture

Think of it like this:

### NAYA
**The intelligence and teacher.**

### MAXIS
**The measurement and mastery engine.**

### CISS
**The compounding learning system that connects everything over time.**

### NAYA POWER ACADEMY
**The achievement and recognition layer.**

Together, they create something much larger than a quiz.

---

# The One-Sentence Version

If someone asks what we're building:

> **Naya Power is an AI-powered personal learning and mastery system that can help you learn what you want, measure what you know, help you improve, and keep compounding your knowledge over time.**

And the simple user experience is:

> **Tell Naya what you want to learn. Let MAXIS show you where you are. Then keep learning and growing.**

---

# NORTH STAR

**This is now the product direction.**

The current MAXIS AI Score is the seed.

The universal MAXIS engine is the measurement system.

Naya is the teacher.

CISS is the compounding loop.

Naya Power Academy is the recognition layer.

The goal is not simply to help people take tests.

The goal is to help people **learn, create, grow, measure progress, and achieve mastery — on whatever path they choose.**

And the first step is beautifully simple:

# **ENTER YOUR NAME. ENTER WHAT YOU WANT TO LEARN. START.**
