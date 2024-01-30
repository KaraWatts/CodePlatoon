import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import { Outlet } from "react-router-dom";
import { Navbar } from "./components/Navbar";

export default function App() {
  return (
    <Container>
      <Row style={{ textAlign: "center" }}>
        <h1>POKEDEX</h1>
      </Row>
      <Navbar />
      <Outlet/>
    </Container>
  );
}
