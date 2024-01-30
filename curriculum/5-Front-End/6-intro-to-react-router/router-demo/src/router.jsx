import { createBrowserRouter, createHashRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./pages/HomePage";
import AboutPage from "./pages/AboutPage";
import ContactPage from './pages/ContactPage';
import NotFountPage from "./pages/NotFoundPage";


// const router = createHashRouter([
const router = createBrowserRouter([
    {
        // http://localhost:5173/
        path: "/",
        element: <App/>,
        children: [
            {
                index: true,
                element: <HomePage/>
            },
            {
                path: 'about/',
                element: <AboutPage />
            },
            {
                path: 'contact/',
                element: <ContactPage />
            },
            // {
            //     path:"*",
            //     element: <NotFountPage/>
            // }
        ],
        errorElement: <NotFountPage />
    }
])

export default router;