
import librarianRoutes from './librarian.js';
import userRoutes from './user.js';
import welcomeRoutes from './welcome.js';

export default [
    ...welcomeRoutes,
    ...userRoutes,
    ...librarianRoutes
]