import WelcomeLayout from "@/views/welcome/Layout.vue"

export default [
    {
        path: '/in',
        component: WelcomeLayout,
        children: [
            {
                path: '', name: 'welcome', component: () => import("@/views/welcome/in.vue")
            }
        ]
    },
    {
        path: '/register',
        component: WelcomeLayout,
        children: [
            {
                path: '', name: 'register', component: () => import("@/views/welcome/register.vue")
            }
        ]
    },
    {
        path: '/login',
        component: WelcomeLayout,
        children: [
            {
                path: '', name: 'login', component: () => import("@/views/welcome/logIn.vue")
            }
        ]
    },
]