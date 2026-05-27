import * as React from 'react'
import Link from 'next/link'

import { cn } from '@/lib/utils'
import { auth } from '@/auth'
import { Button, buttonVariants } from '@/components/ui/button'
import {
  IconGitHub,
  IconNextChat,
  IconSeparator,
  IconVercel
} from '@/components/ui/icons'
import { UserMenu } from '@/components/user-menu'
import { SidebarMobile } from './sidebar-mobile'
import { SidebarToggle } from './sidebar-toggle'
import { ChatHistory } from './chat-history'
import { Session } from '@/lib/types'

async function UserOrLogin() {
  const session = (await auth()) as Session
  return (
    <>
      <Link href="/new" rel="nofollow">
        <IconNextChat className="hidden size-6 mr-2 dark:block" />
      </Link>
      <div className="flex items-center">
        <IconSeparator className="size-6 text-muted-foreground/50" />
        <Button variant="link" asChild className="-ml-2">
          <Link href="/login">Chatbot Demo. Breyner Rojas - Wizeline</Link>
        </Button>
      </div>
    </>
  )
}

export function Header() {
  return (
    ""
  )
}
