import { useState } from "react";
import MySpinner from "./components/Spinner";
import "./App.css";
import NavBar from "./components/NavBar";
import Button from "react-bootstrap/esm/Button";
import MyModal from "./components/MyModal";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col"

function App() {
  //     get     set          init(false)
  const [show, setShow] = useState(false);
  const [modalShow, setModalShow] = useState(false);

  return (
    <>
    <Container>
      <Row className="a-row">Header</Row>
      <Row className="a-row">
        <Col xs={3}>
          left
        </Col>
        <Col xs={6}>
          News feed
        </Col>
        <Col xs={3} >
          Right
        </Col>
      </Row>
      <Row className="a-row">
        Footer
      </Row>
    </Container>
      {/* <NavBar />
      <Button variant="primary" onClick={() => setModalShow(true)}>
        Launch vertically centered modal
      </Button>

      <MyModal show={modalShow} onHide={() => setModalShow(false)} />
      <MySpinner />
      <div className="bg-purple-500 mt-10">
        <p className={show ? "bg-green-200" : "bg-red-200"}>
          Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sed
          consequatur eveniet iusto tempore reprehenderit cum vitae dolor!
          Fugiat animi iusto, tempora, voluptatibus placeat, asperiores
          voluptate explicabo autem numquam accusamus nobis?
        </p>
        <button
          className="px-2 py-1 border-2 text-blue-500 bg-blue-200 hover:bg-blue-300 border-blue-700"
          onClick={() => setShow(!show)}
        >
          Click me!
        </button>
      </div> */}
    </>
  );
}

export default App;
