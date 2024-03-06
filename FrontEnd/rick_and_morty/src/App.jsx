import { Outlet, Link } from "react-router-dom";
// import "./App.css"
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

function App() {
  return (
    <div>
      <Navbar bg="dark" data-bs-theme="dark">
        <Row>
          <Col>
            <Navbar.Brand>
              <Link to="/" style={
                {paddingLeft: "10px",
                  color: "White",
                textDecoration: "none"}
                }>R&M Wiki</Link>
            </Navbar.Brand>
          </Col>
          <Col className="me-auto">
            <Link to="/">Home</Link>
          </Col>
          <Col className="me-auto">
            <Link to="contact/">Contact</Link>
          </Col>
        </Row>
      </Navbar>
      <Outlet />
    </div>
  );
}

export default App;
