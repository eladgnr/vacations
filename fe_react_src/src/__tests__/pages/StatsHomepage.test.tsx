import { render, screen } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import { vi } from 'vitest'
import StatsHomepage from '../../pages/StatsHomepage'
import axios from 'axios'

// Mock axios to prevent real API calls during tests
vi.mock('axios')
const mockedAxios = vi.mocked(axios)

const renderWithRouter = (component: React.ReactElement) => {
    return render(<BrowserRouter>{component}</BrowserRouter>)
}

describe('StatsHomepage', () => {
    beforeEach(() => {
        // Mock the API call that runs in useEffect
        mockedAxios.get.mockRejectedValue(new Error('Not logged in'))
    })

    afterEach(() => {
        vi.clearAllMocks()
    })

    test('renders homepage title with emoji', () => {
        renderWithRouter(<StatsHomepage />)
        expect(screen.getByText(/Statistics Dashboard/)).toBeInTheDocument()
    })

    test('shows about button', () => {
        renderWithRouter(<StatsHomepage />)
        expect(screen.getByText('Learn More About This Project')).toBeInTheDocument()
    })

    test('shows login form when not logged in', () => {
        renderWithRouter(<StatsHomepage />)
        expect(screen.getByPlaceholderText('Username')).toBeInTheDocument()
        expect(screen.getByPlaceholderText('Password')).toBeInTheDocument()
        expect(screen.getByRole('button', { name: 'Login' })).toBeInTheDocument()
    })

    test('renders welcome message', () => {
        renderWithRouter(<StatsHomepage />)
        expect(screen.getByText('Welcome to the statistics site for the Vacations Project.')).toBeInTheDocument()
    })
})