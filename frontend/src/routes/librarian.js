import LibrarianLayout from "@/views/librarian/Layout.vue"

export default [
    {
        path: '/librarian',
        component: LibrarianLayout,
        meta: {
          requiresAuth: true,
          role: ['librarian']
        },
        children: [
          {
            path: '', 
            name: 'librarian-home',
            component: () => import("@/views/librarian/home.vue")
          },
          {
            path: '/requests', 
            name: 'librarian-requests',
            component: () => import("@/views/librarian/requests/requests.vue")
          },
          {
            path: '/books', 
            name: 'librarian-books',
            component: () => import("@/views/librarian/books/books.vue")
          },
          {
            path: '/books/:id',
            name: 'librarian-book',
            component: () => import("@/views/user/books/book.vue")
          },
          {
            path: '/sections', 
            name: 'librarian-sections',
            component: () => import("@/views/librarian/sections/sections.vue")
          },
          {
            path: '/sections/:id',
            name: 'user-section',
            component: () => import("@/views/user/sections/section.vue")
          },
          {
            path: '/authors', 
            name: 'librarian-authors',
            component: () => import("@/views/librarian/authors/authors.vue")
          },
        ]
    }
]