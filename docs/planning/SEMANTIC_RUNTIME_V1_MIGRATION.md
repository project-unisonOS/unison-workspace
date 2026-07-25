# Semantic runtime v1 migration

Legacy `renderer`, `voice`, and `both` choices are compatibility inputs only.
New callers provide `expression-plan-request.v1` with independent input and
output choices plus live modality capabilities and situational context.

Runtime state moves from renderer-local focus to `interaction-session.v1`.
Expressions remain disposable views over SEM; pending actions and confirmations
remain in the modality-neutral session.

Existing experiences enter through `semantic-observation.v1`. Observed content
never carries policy authority. Consequential controls require a separately
authenticated target binding whose person, capability, state version, signature,
and expiry are checked immediately before execution.

During migration, ROM remains an output adapter after SEM construction. New
features must consume SEM, expression plans, and interaction sessions directly.
