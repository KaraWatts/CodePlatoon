import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import AboutPage  from "./pages/AboutPage";
import HomePage from "./pages/HomePage";
import AllCharactersPage from "./pages/AllCharactersPage"
import ACharacterPage from "./pages/ACharacterPage";
import FavoritesPage from "./pages/FavoritesPage";

const router = createBrowserRouter([
    {
        path:'/',
        element: <App />,
        children: [
            {
               index:true,
               element: <HomePage />,
            },
            {
                path:'about/',
                element: <AboutPage/>,
            },
            {
                path:'characters/',
                element: <AllCharactersPage/>,
            },
            {
                path:'character/:id/',
                element: <ACharacterPage/>,
            },
            {
                path:'favorites/',
                element: <FavoritesPage/>
            }
        ]
    }
])

export default router;