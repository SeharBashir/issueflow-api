import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { api } from '../api'
import Modal from '../components/Modal'

export default function Dashboard() {
  const [projects, setProjects] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [showCreate, setShowCreate] = useState(false)
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')
  const [saving, setSaving] = useState(false)
  const navigate = useNavigate()

  useEffect(() => {
    loadProjects()
  }, [])

  async function loadProjects() {
    setLoading(true)
    setError('')
    try {
      const data = await api.getProjects()
      setProjects(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  async function handleCreate(e) {
    e.preventDefault()
    setSaving(true)
    try {
      await api.createProject({ name, description })
      setShowCreate(false)
      setName('')
      setDescription('')
      loadProjects()
    } catch (err) {
      setError(err.message)
    } finally {
      setSaving(false)
    }
  }

  return (
    <div className="container">
      <div className="dash-header">
        <div>
          <h1>Projects</h1>
          <div className="sub">Everything you're tracking, in one place.</div>
        </div>
        <button className="btn btn-primary" onClick={() => setShowCreate(true)}>
          + New project
        </button>
      </div>

      {error && <div className="form-error">{error}</div>}

      {loading ? (
        <div className="loading-text">Loading projects...</div>
      ) : projects.length === 0 ? (
        <div className="empty-state">
          <h3>No projects yet</h3>
          <p>Create your first project to start tracking issues against it.</p>
          <button className="btn btn-primary" onClick={() => setShowCreate(true)}>
            + New project
          </button>
        </div>
      ) : (
        <div className="card-grid">
          {projects.map((p) => (
            <div className="project-card" key={p.id} onClick={() => navigate(`/projects/${p.id}`)}>
              <h3>{p.name}</h3>
              <p>{p.description || 'No description provided.'}</p>
              <div className="meta">
                <span>ID {p.id}</span>
                <span>{new Date(p.created_at).toLocaleDateString()}</span>
              </div>
            </div>
          ))}
        </div>
      )}

      {showCreate && (
        <Modal title="New project" onClose={() => setShowCreate(false)}>
          <form onSubmit={handleCreate}>
            <div className="field">
              <label>Name</label>
              <input value={name} onChange={(e) => setName(e.target.value)} required autoFocus />
            </div>
            <div className="field">
              <label>Description</label>
              <textarea value={description} onChange={(e) => setDescription(e.target.value)} />
            </div>
            <div className="modal-actions">
              <button type="button" className="btn btn-ghost" onClick={() => setShowCreate(false)}>
                Cancel
              </button>
              <button type="submit" className="btn btn-primary" disabled={saving}>
                {saving ? 'Creating...' : 'Create project'}
              </button>
            </div>
          </form>
        </Modal>
      )}
    </div>
  )
}
