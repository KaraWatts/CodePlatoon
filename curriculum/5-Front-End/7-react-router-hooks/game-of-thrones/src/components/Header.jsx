import { Link } from "react-router-dom";

const Header = ({favorites}) => {
  return (
    <>
      <h1>Game of Thrones</h1>
      <nav>
        <Link to="/">Home</Link>
        <Link to="about/">About</Link>
        <Link to="characters/">All Characters</Link>
        <Link to="favorites/">Favorites {favorites.length}</Link>
      </nav>
    </>
  );
};

export default Header;
