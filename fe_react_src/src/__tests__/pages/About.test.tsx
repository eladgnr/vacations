import { render, screen } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import About from '../../pages/About'

const renderWithRouter = (component: React.ReactElement) => {
    return render(<BrowserRouter>{component}</BrowserRouter>)
}

describe('About', () => {
    test('renders project title', () => {
        renderWithRouter(<About />)
        expect(screen.getByText('About This Project')).toBeInTheDocument()
    })

    test('shows back to homepage link', () => {
        renderWithRouter(<About />)
        expect(screen.getByText('← Back to Homepage')).toBeInTheDocument()
    })

    test('displays project overview section', () => {
        renderWithRouter(<About />)
        expect(screen.getByText('Project Overview')).toBeInTheDocument()
    })

    test('shows developer information', () => {
        renderWithRouter(<About />)
        expect(screen.getByText(/Elad K./)).toBeInTheDocument()
    })
})