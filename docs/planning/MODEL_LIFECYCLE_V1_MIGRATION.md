# Model lifecycle v1 migration

Model updates move from direct configuration replacement to an evaluated
deployment record. A candidate progresses through shadow, canary, active, or
rolled-back state. The prior compatible version remains retained until the
rollback window is explicitly closed.

Health signals are aggregate and content-free. They contain contract success,
semantic success, fallback, error, and latency measurements. Person content,
prompts, memories, and model output are excluded.

Hardware compatibility moves from informal sizing guidance to versioned
qualification records. Only complete passing physical-device evidence can
produce a supported model reference. Synthetic and developer-host records stay
visible as engineering evidence and cannot promote support status.
