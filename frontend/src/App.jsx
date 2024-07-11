import react from "react"
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import ProfileCreation from "./components/ProfileCreation"
import StoryCreation from "./components/StoryCreation"
import StoriesList from "./components/StoryCreation"
import Register from "./pages/Register"
import ProtectedRoute from "./components/ProtectedRoute"

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function App() {
  return (
      <><div id="app">
      <h1>MYSPACE</h1>
      <ProfileCreation setCurrentProfileId={setCurrentProfileId} />
      {currentProfileId && (
        <StoryCreation
          currentProfileId={currentProfileId}
          reloadStories={() => window.location.reload()} />
      )}
      <StoriesList />
    </div><BrowserRouter>
        <Routes>
          <Route
            path="/"
            element={<ProtectedRoute>
              <Home />
            </ProtectedRoute>} />
          <Route path="/Register" element={<Register />} />
          <Route path="*" element={<NotFound />}></Route>
        </Routes>
      </BrowserRouter></>
  )
}

export default App
