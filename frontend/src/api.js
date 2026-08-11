const BASE_URL = 'http://127.0.0.1:8000'

function getToken() {
  return localStorage.getItem('issueflow_token')
}

export function setToken(token) {
  if (token) {
    localStorage.setItem('issueflow_token', token)
  } else {
    localStorage.removeItem('issueflow_token')
  }
}

async function request(path, { method = 'GET', body, auth = true, form = false } = {}) {
  const headers = {}
  if (!form) headers['Content-Type'] = 'application/json'

  if (auth) {
    const token = getToken()
    if (token) headers['Authorization'] = `Bearer ${token}`
  }

  const res = await fetch(`${BASE_URL}${path}`, {
    method,
    headers,
    body: form ? body : body ? JSON.stringify(body) : undefined,
  })

  if (res.status === 204) return null

  let data = null
  try {
    data = await res.json()
  } catch {
    data = null
  }

  if (!res.ok) {
    const message = data?.detail
      ? (Array.isArray(data.detail) ? data.detail.map(d => d.msg).join(', ') : data.detail)
      : 'Something went wrong. Please try again.'
    throw new Error(message)
  }

  return data
}

export const api = {
  register: (email, password) =>
    request('/auth/register', { method: 'POST', body: { email, password }, auth: false }),

  login: (email, password) => {
    const form = new URLSearchParams()
    form.append('username', email)
    form.append('password', password)
    return request('/auth/login', { method: 'POST', body: form, auth: false, form: true })
  },

  getProjects: () => request('/projects/'),
  getProject: (id) => request(`/projects/${id}`),
  createProject: (data) => request('/projects/', { method: 'POST', body: data }),
  updateProject: (id, data) => request(`/projects/${id}`, { method: 'PUT', body: data }),
  deleteProject: (id) => request(`/projects/${id}`, { method: 'DELETE' }),

  getIssuesByProject: (projectId) => request(`/issues/project/${projectId}`),
  createIssue: (data) => request('/issues/', { method: 'POST', body: data }),
  updateIssue: (id, data) => request(`/issues/${id}`, { method: 'PUT', body: data }),
  deleteIssue: (id) => request(`/issues/${id}`, { method: 'DELETE' }),
}
