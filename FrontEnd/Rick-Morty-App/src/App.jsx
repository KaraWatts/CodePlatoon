import { Outlet, Link } from "react-router-dom";
import { Navbar, Nav, Row, Col, Container } from "react-bootstrap";
import "./App.css";

function App() {
  return (
    <>
      <div>
        <Navbar bg="dark" data-bs-theme="dark">
          <Navbar.Brand>
              <Link to={"/"} style={{
                textDecoration: 'none',
                paddingLeft: "10px",
                color: "white"
              }}>Rick and Morty</Link>
          </Navbar.Brand>
          <Nav>
            <Link to={"about/"} style={{
                textDecoration: 'none',
                marginLeft: "2px",
                marginRight: "10px",
                color: "white"
              }}>About</Link>
          </Nav>
          <Nav>
            <Link to={"characters/"} style={{
                textDecoration: 'none',
                color: "white"
              }}>Characters</Link>
          </Nav>
        </Navbar>
        <Outlet />
      </div>
    </>
  );
}

export default App;
