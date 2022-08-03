import './App.css'
import { MantineProvider, Text } from '@mantine/core'
import HomeScreen from './UI/home_screen'

function App() {
  return (
    <MantineProvider withGlobalStyles withNormalizeCSS>
      <HomeScreen/>
    </MantineProvider>
  )
}

export default App
