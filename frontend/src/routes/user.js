import UserLayout from "@/views/user/Layout.vue"

export default [
    {
        path: '/',
        component: UserLayout,
        meta: {
            requiresAuth: true,
            role: ['user'],
        },
        children: [
            {
                path: '',
                name: 'user-home',
                component: () => import("@/views/user/home.vue")
            },
            {
                path:'requests',
                name: 'user-requests',
                component: () => import("@/views/user/requests/requests.vue")
            },
            {
                path:'books',
                name: 'user-books',
                component: () => import("@/views/user/books/books.vue"),
            },
            {
                path: 'books/:id',
                name: 'user-book',
                component: () => import("@/views/user/books/book.vue"),
            },
            {
                path: 'sections',
                name: 'user-sections',
                component: () => import("@/views/user/sections/sections.vue")
            },
            {
                path: 'sections/:id',
                name: 'user-section',
                component: () => import("@/views/user/sections/section.vue")
            },
            {
                path: 'authors',
                name: 'user-authors',
                component: () => import("@/views/librarian/authors/authors.vue")
            },
            {
                path: 'author/:id',
                name: 'user-author',
                component: () => import("@/views/librarian/authors/author.vue")
            },
        ]
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'not-found',
        component: () => import("@/views/NotFound.vue")
    }
]
    