import "./App.css";
import { Outlet, Link } from "react-router-dom";

function App() {
  // only render homepage if I'm currently in localhost:5173/
  return (
    <>
      <h1>Hello Victor</h1>
      <nav>
        <ul>
          <li>
            <Link to='/'>Home</Link>
          </li>
          <li>
            <Link to='about/'>About</Link>
          </li>
          <li>
            <Link to="contact/">Contact</Link>
          </li>
        </ul>
      </nav>
      <Outlet />
    </>
  );
}

export default App;
