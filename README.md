# dronetag-assignment

## How to run
1.  copy and rename `.env.example` as `.env` (and change values as desired)
2. `docker compose -f docker-compose.local.yml build`
3. `docker compose -f docker-compose.local.yml up -d`

User `admin` with password `admin` is automatically created.

## TODO
- [ ] flight analytics dataset list view
- [ ] flight analytics dataset detail view (charts using chart.js)
- [ ] JSON REST API using Django ninja
- [ ] Logging
- [ ] Tests (using pytest)
- [ ] Locked requirements.txt 👉 requirements.lock
- [ ] ...
