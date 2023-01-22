import { useEffect } from 'react'
import './App.scss'
import Sidebar from './components/sidebar'


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
      <Sidebar />
    </div>
  )
}

export default App
