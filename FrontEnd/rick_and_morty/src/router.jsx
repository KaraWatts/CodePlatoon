import { createBrowserRouter } from "react-router-dom";
import App from './App';
import HomePage from "./pages/HomePage";
import Contact from "./pages/Contact";

const router = createBrowserRouter([
    {
        path:"/",
        element: <App />,
        children: [
            {
                index: true,
                element: <HomePage />,
            },
            {
                path: "contact",
                element: <Contact />,
            },
        ],
    },
]);

export default router