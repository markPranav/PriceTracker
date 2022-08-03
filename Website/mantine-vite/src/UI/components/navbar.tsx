import { Navbar, Group, Code, ScrollArea, createStyles, Menu } from '@mantine/core';
import { Icon2fa, IconBellRinging, IconDatabaseImport, IconFingerprint, IconKey, IconLogout, IconReceipt2, IconSettings, IconSwitchHorizontal } from '@tabler/icons';
import { useState } from 'react';
import { UserButton } from './userButton';


const mockdata = [
  { link: '', label: 'Notifications', icon: IconBellRinging },
  { link: '', label: 'Billing', icon: IconReceipt2 },
  { link: '', label: 'Security', icon: IconFingerprint },
  { link: '', label: 'SSH Keys', icon: IconKey },
  { link: '', label: 'Databases', icon: IconDatabaseImport },
  { link: '', label: 'Authentication', icon: Icon2fa },
  { link: '', label: 'Other Settings', icon: IconSettings },
]


const useStyles = createStyles((theme, _params, getRef) => {
  const icon: string = getRef('icon');
  return {
    navbar: {
      backgroundColor: theme.colorScheme === 'dark' ? theme.colors.dark[6] : theme.white,
      paddingBottom: 0,
    },
    link: {
      ...theme.fn.focusStyles(),
      display: 'flex',
      alignItems: 'center',
      textDecoration: 'none',
      fontSize: theme.fontSizes.sm,
      color: theme.colorScheme === 'dark' ? theme.colors.dark[1] : theme.colors.gray[7],
      padding: `${theme.spacing.xs}px ${theme.spacing.sm}px`,
      borderRadius: theme.radius.sm,
      fontWeight: 500,

      '&:hover': {
        backgroundColor: theme.colorScheme === 'dark' ? theme.colors.dark[6] : theme.colors.gray[0],
        color: theme.colorScheme === 'dark' ? theme.white : theme.black,

        [`& .${icon}`]: {
          color: theme.colorScheme === 'dark' ? theme.white : theme.black,
        },
      },
    },

    linkIcon: {
      ref: icon,
      color: theme.colorScheme === 'dark' ? theme.colors.dark[2] : theme.colors.gray[6],
      marginRight: theme.spacing.sm,
    },

    linkActive: {
      '&, &:hover': {
        backgroundColor: theme.fn.variant({ variant: 'light', color: theme.primaryColor })
          .background,
        color: theme.fn.variant({ variant: 'light', color: theme.primaryColor }).color,
        [`& .${icon}`]: {
          color: theme.fn.variant({ variant: 'light', color: theme.primaryColor }).color,
        },
      },
    },

    footer: {
      padding: theme.spacing.sm,
      marginLeft: -theme.spacing.md,
      marginRight: -theme.spacing.md,
      borderTop: `1px solid ${
        theme.colorScheme === 'dark' ? theme.colors.dark[4] : theme.colors.gray[3]
      }`,
    },
  }
});

interface NavbarProps {
  hidden: boolean;
  activeLink: string;
}

export function NavbarSimple({hidden, activeLink}: NavbarProps) {
  
  const [active, setActive] = useState(activeLink);
  const { classes, cx } = useStyles();
  const links = mockdata.map((item) => <a
    className={cx(classes.link, { [classes.linkActive]: item.label === active })}
    href={item.link}
    key={item.label}
    onClick={(event) => {
      event.preventDefault();
      setActive(item.label);
    }}
  >
    <item.icon className={classes.linkIcon} stroke={1.5} />
    <span>{item.label}</span>
  </a>);

  return (
    <Navbar pt="md" px="md" hiddenBreakpoint="sm" hidden={hidden} width={{ sm: 270, lg: 320 }} className={classes.navbar} >

      <Navbar.Section grow component={ScrollArea}>
        {links}
      </Navbar.Section>
      <Navbar.Section className={classes.footer}>
        <UserButton
          image="https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=255&q=80"
          name="Guest"
          email="Sign in"/>
      </Navbar.Section>
    </Navbar>
  );
}

