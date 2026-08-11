import { Link } from 'react-router-dom'
import StatusBadge from '../components/StatusBadge'

const MOCK_ISSUES = [
  { id: 'ISS-104', title: 'API returns 500 on bulk delete', priority: 'high', status: 'open' },
  { id: 'ISS-101', title: 'Dashboard chart mislabels Q3 totals', priority: 'medium', status: 'in_progress' },
  { id: 'ISS-098', title: 'Slow query on project list endpoint', priority: 'medium', status: 'resolved' },
  { id: 'ISS-092', title: 'Typo in password reset email', priority: 'low', status: 'closed' },
]

const FEATURES = [
  {
    tag: '01',
    title: 'Token-based access',
    body: 'Every route is authenticated with JWT. Register, log in, and every request after that carries a signed token.',
  },
  {
    tag: '02',
    title: 'Guarded status transitions',
    body: 'Issues can\u2019t jump straight from open to closed. State changes follow a defined workflow, enforced server-side.',
  },
  {
    tag: '03',
    title: 'Linked by design',
    body: 'Every issue belongs to a project through a real ORM relationship \u2014 not a loose reference, an actual foreign key.',
  },
  {
    tag: '04',
    title: 'Traceable by default',
    body: 'created_at and updated_at are stamped automatically, so nothing changes without leaving a timestamp behind.',
  },
  {
    tag: '05',
    title: 'Config outside the code',
    body: 'Database URL, secrets, and environment settings live in .env \u2014 never hardcoded, never committed.',
  },
  {
    tag: '06',
    title: 'Consistent failure states',
    body: 'Every error \u2014 missing resource, bad transition, invalid login \u2014 returns the same shape, every time.',
  },
]

export default function Landing() {
  return (
    <>
      <section className="hero">
        <div className="container">
          <div style={{ display: 'grid', gridTemplateColumns: '1fr', gap: 56 }}>
            <div>
              <div className="eyebrow">
                <span className="brand-lamp" style={{ width: 6, height: 6 }} />
                Status: all systems operational
              </div>
              <h1>
                Track issues before they<br />
                become <span className="accent-text">incidents.</span>
              </h1>
              <p className="lede">
                IssueFlow is a backend-first issue and incident tracker: authenticated
                API, enforced workflows, and a clean data model underneath a simple
                board.
              </p>
              <div className="hero-actions">
                <Link to="/register" className="btn btn-primary">Create an account</Link>
                <Link to="/login" className="btn btn-secondary">Log in</Link>
              </div>
            </div>

            <div className="board-mock">
              <div className="board-mock-header">
                <span>project / website-redesign / issues</span>
                <div className="board-dots">
                  <span /><span /><span />
                </div>
              </div>
              {MOCK_ISSUES.map((issue) => (
                <div className="board-row" key={issue.id}>
                  <span className="board-id">{issue.id}</span>
                  <span className="board-title">{issue.title}</span>
                  <span className={`board-priority priority-${issue.priority}`}>{issue.priority}</span>
                  <StatusBadge status={issue.status} />
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section className="section">
        <div className="container">
          <div className="section-label">What's actually built</div>
          <h2>A small API, built the way a real one would need to work.</h2>
          <div className="grid-3">
            {FEATURES.map((f) => (
              <div className="feature-card" key={f.tag}>
                <div className="icon-lamp">{f.tag}</div>
                <h3>{f.title}</h3>
                <p>{f.body}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="section" style={{ paddingTop: 0 }}>
        <div className="container">
          <div className="section-label">Under the hood</div>
          <h2 style={{ marginBottom: 20 }}>Built with</h2>
          <div className="stack-strip">
            {['FastAPI', 'SQLAlchemy', 'Pydantic', 'JWT / OAuth2', 'Passlib (bcrypt)', 'SQLite', 'React', 'Vite'].map((t) => (
              <span className="stack-chip" key={t}>{t}</span>
            ))}
          </div>
        </div>
      </section>

      <footer className="footer">
        <div className="container" style={{ display: 'flex', justifyContent: 'space-between' }}>
          <span>IssueFlow \u2014 built as a backend engineering exercise</span>
          <span>2026</span>
        </div>
      </footer>
    </>
  )
}
