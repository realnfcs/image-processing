import './App.css'

import { BrowserRouter, Routes, Route } from 'react-router-dom'

import SideBar from './components/sidebar/SideBar.jsx'
import NavBar from './components/navbar/NavBar.jsx'
import Home from  './components/home/Home.jsx'
import Algebraic from './components/algebraic/Algebraic.jsx'
import Convolution from './components/convolution/Convolution.jsx'
import EdgeDetectention from './components/edgeDetectention/EdgeDetectention.jsx'
import Filters from './components/filters/Filters.jsx'
import Geometric from './components/geometric/Geometric.jsx'
import Histogram from './components/histogram/Histogram.jsx'
import IntensityTransformation from './components/intensityTransformation/IntensityTransformation.jsx'
import Sharpening from './components/sharpening/Sharpening.jsx'

function App() {

  return (
    <div className="App">
      <BrowserRouter>
        <SideBar />
      <Routes>
        <Route path='/' element={ <Home /> } />
        <Route path='/algebraic' element={ <Algebraic /> } />
        <Route path='/convolution' element={ <Convolution /> } />
        <Route path='/edge-detectention' element={ <EdgeDetectention /> } />
        <Route path='/filters' element={ <Filters /> } />
        <Route path='/geometric' element={ <Geometric /> } />
        <Route path='/histogram' element={ <Histogram />} />
        <Route path='/intensity-transformations' element={ <IntensityTransformation /> } />
        <Route path='/sharpening' element={ <Sharpening /> } />
      </Routes>
      </BrowserRouter>

      <NavBar />

   </div>
  )
}

export default App
