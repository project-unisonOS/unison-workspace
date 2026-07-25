# Phase 11 private life operations runbook

Status: software operations baseline, 2026-07-25

## Support triage

1. Confirm the authenticated person and affected private space without asking
   for document content, credentials, full account identifiers, or diagnoses.
2. Record the source, import session, connection, sync receipt, domain record,
   or brief identifier needed to trace the failure.
3. Pause the affected import or revoke the affected connection. Do not broaden
   scopes or move data into a shared space to diagnose a failure.
4. Export only the person's requested source or privacy-minimized diagnostic
   receipt through the authenticated local experience.
5. Escalate a suspected cross-person disclosure, unsafe action, credential
   exposure, parser escape, or document-instruction execution immediately.

## Import and parser recovery

1. Leave failed bytes in encrypted quarantine and outside retrieval.
2. Record media signature, parser version, OCR version, source checksum, and
   failure class without logging extracted personal content.
3. Resume from the last import checkpoint when parser policy is unchanged.
4. Roll back the session when deterministic recovery is not possible.
5. Test parser updates against the synthetic normal, malformed, archive,
   prompt-injection, malware, household, health, and finance corpus.
6. Reprocess only after the person reviews changed extraction and destination.

## Connector revocation and recovery

1. Mark the connection inactive before attempting provider cleanup.
2. Remove its refresh credential through the per-person credential handle.
3. Clear cursors and block new sync receipts.
4. Show whether already imported records remain, then let the person retain or
   delete them explicitly.
5. On outage or expired consent, preserve the last receipt and cursor. Resume
   idempotently after renewed consent without duplicate provider IDs.
6. Treat changed issuer, audience, redirect, scope, or provider identity as a
   new connection requiring review.

## Correction and deletion

1. Preserve original source bytes and create a person-authored correction on
   the derived field or record.
2. Regenerate affected attention and briefs with citations to the correction.
3. Source deletion removes encrypted bytes, extracted fields, derived domain
   records, affected links, and attention indexes for that source.
4. Unlinking two domains removes only the link and preserves both sources.
5. Verify search, timeline, attention, brief, and export paths no longer return
   deleted material.

## Health safety incident

1. Do not interpret symptoms or tell the person an emergency is ruled out.
2. Present deterministic seek-help guidance for a matched urgent fixture.
3. Disable a package if it asserted a diagnosis, treatment or medication
   change, or emergency dismissal.
4. Preserve privacy-minimized rule, source, and response identifiers.
5. Require health-safety review and corpus replay before restoration.

## Financial safety incident

1. Stop attempts at money movement, investment, credit, filing, account
   closure, or autonomous dispute submission.
2. Revoke any connection that requested a write scope.
3. Verify no private account entered a shared total without an explicit
   contribution record.
4. Preserve minimized receipts and recalculate from cited statements.
5. Require financial-safety review before restoring an adapter or rule.

## Cross-domain or privacy incident

1. Remove the affected purpose-bound link without deleting source records.
2. Revoke external drafts and connection access associated with the incident.
3. Identify exact fields, recipients, domains, person, and space involved.
4. Notify the affected person locally with correction and deletion options.
5. Replay cross-person, private-plus-shared, prompt-injection, credential, and
   deletion tests before restoration.

## Pilot and promotion

Human pilots require explicit opt-in and may stop at any time. Record aggregate
metrics without source content. Any boundary incident or unsafe action fails the
pilot gate. A named human reviewer must separately approve each domain package
and live provider. The default decision is hold.
