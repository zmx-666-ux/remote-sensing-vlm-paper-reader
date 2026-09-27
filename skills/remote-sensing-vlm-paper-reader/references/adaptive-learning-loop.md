# Adaptive learning and post-reading feedback

Use this procedure after the learner submits answers, questions, reflections, or candidate research ideas about a paper. Its purpose is to improve later reading, not to reward fluent wording or inflate novelty.

## 1. Diagnose each statement

Assign exactly one primary verdict and explain it:

- `correct and transferable` — accurate mechanism and usable beyond the current wording;
- `partially correct` — central intuition is sound but a mechanism, condition, or boundary is missing;
- `incorrect` — conflicts with the paper or established mechanism;
- `unsupported inference` — plausible, but the cited evidence does not establish it;
- `testable research hypothesis` — can be falsified by a specified comparison;
- `novelty unresolved` — promising idea that still needs a separate literature search.

For each answer, report: what is right, what is missing, a corrected formulation, and one short transfer check. Do not equate longer answers with stronger understanding.

## 2. Locate the source of difficulty

Classify gaps using these dimensions:

1. **Representation and shapes** — token, sequence, feature map, region, global vector, batch matrix.
2. **Objective and supervision** — where positives, negatives, labels, pseudo-labels, or consistency signals come from.
3. **Mechanism-to-output chain** — which operation turns an input signal into a region, mask, class, or text output.
4. **Evidence boundary** — paper result versus interpretation, feasibility, trend, or novelty claim.
5. **Reproduction readiness** — ability to state inputs, frozen/trainable modules, losses, evaluation, and a smallest credible run.
6. **Research transfer** — ability to form a useful hypothesis without skipping controls or failure conditions.

Look for repeated reasoning patterns across answers. Distinguish conceptual intuition from implementation readiness.

## 3. Update the private learner profile

Only update a profile in the user's private research library. Never copy personal answers, scores, paths, unpublished ideas, or a populated profile into the public Plugin repository.

For each dimension, store:

- status: `mastered`, `developing`, or `weak`;
- dated evidence from the learner's answer;
- misconception or missing link;
- next-reading treatment: `compress`, `normal`, or `expand`;
- one observable condition for promotion to the next status.

Do not downgrade a skill from one ambiguous response alone. Do not mark a concept `mastered` until the learner explains it accurately and transfers it to a new example.

## 4. Adapt the next paper note

Keep the public note schema stable, but change emphasis:

- compress concepts supported by recent mastery evidence;
- expand `developing` and `weak` mechanisms using tensor shapes and one concrete example;
- trace source signal → representation → operation → objective → output;
- require controls that reveal whether a modality is ignored, such as correct text, shuffled text, contradictory text, and no text;
- distinguish global, region, and pixel granularity;
- include one implementation question and one transfer question.

Do not overfit an entire note to a single mistake. The paper's own contribution and decisive evidence remain primary.

## 5. Evaluate research ideas

Separate five layers:

1. observation or task pain point;
2. proposed mechanism;
3. nearest known overlap;
4. minimum discriminating experiment and controls;
5. result that would falsify or downgrade the idea.

Never call an idea novel before a dedicated search. When a learner moves from possibility to field-wide prevalence, explicitly request or perform current literature verification.

## 6. Artifact policy

- The original evidence-grounded note remains valid unless it contains a factual error.
- Add post-reading feedback to the same note only when the user requests document integration.
- Otherwise, give the diagnosis in conversation and update only the private learner profile.
- Preserve the stable paper ID and filename; do not create `v2`, `修订版`, or duplicate files by default.
- Report exactly which private and public artifacts were changed.
