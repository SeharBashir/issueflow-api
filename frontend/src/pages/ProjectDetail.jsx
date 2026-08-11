import { useEffect, useState } from 'react'
import { useParams, useNavigate, Link } from 'react-router-dom'
import { api } from '../api'
import Modal from '../components/Modal'
import StatusBadge from '../components/StatusBadge'

const STATUS_OPTIONS = ['open', 'in_progress', 'resolved', 'closed']

export default function ProjectDetail() {
  const { projectId } = useParams()
  const navigate = useNavigate()

  const [project, setProject] = useState(null)
  const [issues, setIssues] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  const [showCreate, setShowCreate] = useState(false)
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const [priority, setPriority] = useState('medium')
  const [saving, setSaving] = useState(false)

  useEffect(() => {
    load()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [projectId])

  async function load() {
    setLoading(true)
    setError('')
    try {
      const [proj, iss] = await Promise.all([
        api.getProject(projectId),
        api.getIssuesByProject(projectId),
      ])
      setProject(proj)
      setIssues(iss)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  async function handleCreateIssue(e) {
    e.preventDefault()
    setSaving(true)
    setError('')
    try {
      await api.createIssue({
        title,
        description,
        priority,
        project_id: Number(projectId),
      })
      setShowCreate(false)
      setTitle('')
      setDescription('')
      setPriority('medium')
      load()
    } catch (err) {
      setError(err.message)
    } finally {
      setSaving(false)
    }
  }

  async function handleStatusChange(issue, newStatus) {
    setError('')
    try {
      await api.updateIssue(issue.id, { status: newStatus })
      load()
    } catch (err) {
      setError(err.message)
    }
  }

  async function handleDeleteIssue(issueId) {
    if (!confirm('Delete this issue? This cannot be undone.')) return
    setError('')
    try {
      await api.deleteIssue(issueId)
      load()
    } catch (err) {
      setError(err.message)
    }
  }

  async function handleDeleteProject() {
    if (!confirm('Delete this project and all its issues? This cannot be undone.')) return
    setError('')
    try {
      await api.deleteProject(projectId)
      navigate('/dashboard')
    } catch (err) {
      setError(err.message)
    }
  }

  if (loading) {
    return (
      <div className="container">
        <div className="loading-text">Loading project...</div>
      </div>
    )
  }

  return (
    <div className="container">
      <div className="detail-header">
        <Link to="/dashboard" className="back-link">&larr; All projects</Link>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
          <div>
            <h1>{project?.name}</h1>
            <p>{project?.description || 'No description provided.'}</p>
          </div>
          <button className="btn btn-danger btn-sm" onClick={handleDeleteProject}>
            Delete project
          </button>
        </div>
      </div>

      {error && <div className="form-error">{error}</div>}

      <div className="detail-toolbar">
        <h2>{issues.length} issue{issues.length === 1 ? '' : 's'}</h2>
        <button className="btn btn-primary btn-sm" onClick={() => setShowCreate(true)}>
          + New issue
        </button>
      </div>

      {issues.length === 0 ? (
        <div className="empty-state">
          <h3>No issues yet</h3>
          <p>Log the first issue for this project.</p>
          <button className="btn btn-primary" onClick={() => setShowCreate(true)}>
            + New issue
          </button>
        </div>
      ) : (
        <div className="issue-list">
          {issues.map((issue) => (
            <div className="issue-row" key={issue.id}>
              <div>
                <span className="issue-id">#{issue.id}</span>
                <span className="issue-title">{issue.title}</span>
              </div>
              <span className={`priority-tag priority-${issue.priority}`}>{issue.priority}</span>
              <StatusBadge status={issue.status} />
              <div className="row-actions">
                <select
                  className="status-select"
                  value={issue.status}
                  onChange={(e) => handleStatusChange(issue, e.target.value)}
                >
                  {STATUS_OPTIONS.map((s) => (
                    <option key={s} value={s}>{s}</option>
                  ))}
                </select>
                <button className="btn btn-danger btn-sm" onClick={() => handleDeleteIssue(issue.id)}>
                  Delete
                </button>
              </div>
            </div>
          ))}
        </div>
      )}

      {showCreate && (
        <Modal title="New issue" onClose={() => setShowCreate(false)}>
          <form onSubmit={handleCreateIssue}>
            <div className="field">
              <label>Title</label>
              <input value={title} onChange={(e) => setTitle(e.target.value)} required autoFocus />
            </div>
            <div className="field">
              <label>Description</label>
              <textarea value={description} onChange={(e) => setDescription(e.target.value)} />
            </div>
            <div className="field">
              <label>Priority</label>
              <select value={priority} onChange={(e) => setPriority(e.target.value)}>
                <option value="low">Low</option>
                <option value="medium">Medium</option>
                <option value="high">High</option>
              </select>
            </div>
            <div className="modal-actions">
              <button type="button" className="btn btn-ghost" onClick={() => setShowCreate(false)}>
                Cancel
              </button>
              <button type="submit" className="btn btn-primary" disabled={saving}>
                {saving ? 'Creating...' : 'Create issue'}
              </button>
            </div>
          </form>
        </Modal>
      )}
    </div>
  )
}
