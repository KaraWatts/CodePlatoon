import { createBrowserRouter } from "react-router-dom";
import App from "./App"
import HomePage from "./pages/HomePage";
import AboutPage from "./pages/AboutPage";
import Characters from "./pages/CharactersPage";
import NotFound from "./pages/NotFound";



const router = createBrowserRouter([
        {
            path: '/',
            element: <App/>,
            children: [
                {
                    index:true,
                    element: <HomePage/>
                },
                {
                    path:"about/",
                    element:<AboutPage/>
                },
                {
                    path:"characters/",
                    element:<Characters/>
                }
            ],
            errorElement: <NotFound />
        },




]);

export default router;