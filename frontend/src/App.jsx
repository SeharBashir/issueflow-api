import { useState } from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Navbar from './components/Navbar'
import Landing from './pages/Landing'
import Login from './pages/Login'
import Register from './pages/Register'
import Dashboard from './pages/Dashboard'
import ProjectDetail from './pages/ProjectDetail'

function hasToken() {
  return Boolean(localStorage.getItem('issueflow_token'))
}

function ProtectedRoute({ isAuthed, children }) {
  if (!isAuthed) return <Navigate to="/login" replace />
  return children
}

export default function App() {
  const [isAuthed, setIsAuthed] = useState(hasToken())

  return (
    <BrowserRouter>
      <div className="page">
        <Navbar isAuthed={isAuthed} />

        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/login" element={<Login onAuthed={() => setIsAuthed(true)} />} />
          <Route path="/register" element={<Register onAuthed={() => setIsAuthed(true)} />} />
          <Route
            path="/dashboard"
            element={
              <ProtectedRoute isAuthed={isAuthed}>
                <Dashboard />
              </ProtectedRoute>
            }
          />
          <Route
            path="/projects/:projectId"
            element={
              <ProtectedRoute isAuthed={isAuthed}>
                <ProjectDetail />
              </ProtectedRoute>
            }
          />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </div>
    </BrowserRouter>
  )
}
