import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Navbar from './component/navbar';
import Home from './pages/home';

function App() {
  return (
    <Router>
      <Navbar/>
      <Routes>
        <Route path="/">
          <Route index element={<Home/>} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
