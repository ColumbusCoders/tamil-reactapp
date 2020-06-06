import React from 'react'
import {Nav,Navbar,Form,FormControl,Button,NavDropdown} from 'react-bootstrap'


class Navmenu extends React.Component{

    render() {
        return (
            <div>
                    <Navbar sticky="top" bg="light" expand="lg">
                    <Navbar.Brand href="/">தமிழ் கதம்பம்</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="mr-auto">
                        <Nav.Link href="/Politics">அரசியல்</Nav.Link>
                        <Nav.Link href="/Business">வணிகம்</Nav.Link>
                        <Nav.Link href="/Cinema">சினிமா</Nav.Link>
                        <Nav.Link href="/Divine">ஆன்மீகம்</Nav.Link>
                        <Nav.Link href="/Sports">விளையட்டு</Nav.Link>
                        </Nav>
                    </Navbar.Collapse>
                    </Navbar>
            </div>
        );
      }

}

export default Navmenu