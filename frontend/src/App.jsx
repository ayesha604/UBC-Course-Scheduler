import { useEffect } from 'react'
import './App.scss'
import Nav from './components/Nav'

const prefetchCourseURL = 'http://127.0.0.1:5000/valid_courses'

function App() {

  useEffect(() => {
    async function prefetch() {
      try {
        let response = (await fetch(prefetchCourseURL))
        console.log(await response.text())
      } catch(e) {
        console.error("Network request failed")
      }
    }
    prefetch()
  }, [])

  
  return (
    <div className="App">
      <Nav />
    </div>
  )
}

export default App
