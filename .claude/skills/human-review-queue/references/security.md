# Security boundary

## Local modes

Use `single_local` while one person reviews all work. The server ignores browser-selected identity and uses `default_reviewer`.

Use `local_switcher` only on loopback for development or a trusted single-user workstation. A reviewer selector is routing convenience, not authentication.

The local server must bind to `127.0.0.1`. Keep the same-origin check, request token, CSP, response size limit, and no-store headers enabled.

## Authenticated mode

Use `trusted_header` only behind an authenticated reverse proxy. The proxy must remove any client-supplied identity header and set the trusted header after authentication. Map the value to one active reviewer ID.

Before network access, define:

- authentication and account recovery
- TLS termination
- reviewer and administrator authorization
- source visibility
- CSRF and session behavior
- audit logs and alerting
- response and media retention
- backup and restore
- reviewer removal and reassignment
- incident response

The included server is not a complete public deployment.

## Dispatch

Keep dispatch disabled during installation and tests. Enable it only after the user approves the adapter, destination repository, label, action boundary, and service account.

Do not place tokens in config, queue entries, runtime JSON, logs, or agent prompts. Use the platform credential store. A failed dispatch must leave the Queue Response and decision record intact.

## Media

Serve only files under an approved source root. Use direct HTTPS links for artifacts outside that root. Do not copy sensitive media into the queue without a purpose, consent basis, retention rule, and deletion path.
