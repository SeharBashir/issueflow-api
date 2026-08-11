import { Link, useNavigate } from 'react-router-dom'
import { setToken } from '../api'

export default function Navbar({ isAuthed }) {
  const navigate = useNavigate()

  function handleLogout() {
    setToken(null)
    navigate('/login')
  }

  return (
    <div className="navbar">
      <div className="container navbar-inner">
        <Link to="/" className="brand">
          <span className="brand-lamp" />
          IssueFlow
        </Link>

        {isAuthed ? (
          <div className="top-nav-user">
            <Link to="/dashboard" className="btn btn-ghost btn-sm">Dashboard</Link>
            <button className="btn btn-secondary btn-sm" onClick={handleLogout}>Log out</button>
          </div>
        ) : (
          <div className="nav-links">
            <Link to="/login">Log in</Link>
            <Link to="/register" className="btn btn-primary btn-sm">Get started</Link>
          </div>
        )}
      </div>
    </div>
  )
}
