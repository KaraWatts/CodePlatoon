import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import { Link, useNavigate } from "react-router-dom";

function CharCard({ id, name, image, setFavorites, favorites }) {
  const navigate = useNavigate();

  const shouldRoute = (id) => {
    navigate(`/character/${id}/`);
  };

  return (
    <Card style={{ width: "18rem" }}>
      <Card.Img variant="top" src={image} />
      <Card.Body>
        <Card.Title>{name}</Card.Title>
        {/* <Link to={`/character/${id}/`}> */}
        <Button variant="primary" onClick={() => shouldRoute(id)}>
          Details
        </Button>
        <Button
          variant="warning"
          onClick={() =>
            setFavorites([...favorites, { id: id, name: name, image: image }])
          }
        >
          Favorite
        </Button>
        {/* </Link> */}
      </Card.Body>
    </Card>
  );
}

export default CharCard;
