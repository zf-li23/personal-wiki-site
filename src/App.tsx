import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import Home from './pages/Home';
import Wiki from './pages/Wiki';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="wiki/*" element={<Wiki />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
