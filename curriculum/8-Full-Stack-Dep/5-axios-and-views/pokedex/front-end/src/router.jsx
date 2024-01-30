import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import { Pokemon } from "./pages/Pokemon";
import { Home } from "./pages/Home";
import { Moves } from "./pages/Moves";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        index: true,
        element: <Home />,
      },
      {
        path: "pokemon",
        element: <Pokemon/>,
      },
      {
        path: "moves",
        element: <Moves />,
      },
    ],
  },
]);

export default router;
