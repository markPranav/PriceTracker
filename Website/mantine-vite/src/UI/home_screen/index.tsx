import { AppShell, Text } from '@mantine/core'
import { HeaderSimple } from '../components/header'
import { NavbarMinimal } from '../components/navbar'

type Props = {}

function HomeScreen({}: Props) {
  return (
    <AppShell
        header={ <HeaderSimple user={{name: "Sign In", image: "https://picsum.photos/200"}}/>}
        navbar={<NavbarMinimal hidden={false}/>}
        navbarOffsetBreakpoint="sm"
        >
        <Text>Helloslichowe</Text>
    </AppShell>
  )
}

export default HomeScreen