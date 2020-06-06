import React from 'react'
import {Nav,Navbar,Form,FormControl,Button,NavDropdown} from 'react-bootstrap'
import {Container,Col,Row,Card,CardDeck,CardColumns} from 'react-bootstrap';


class CardDisplay extends React.Component{

    render() {
        return (
            <div widh="%100" >
                <Container fluid="true">
                <div className="flexwrap flex flex-row"> 
                {this.props.feedResults.map(result => (
                                <a href={result.link} className="flex-grid-item card flex-grid-item standard-card flex flex-column">
                                    <table>
                                        <tr>
                                            <td>  
                                                 <img className="images" src={result.imagelink} />
                                            </td>
                                            <td> 
                                                <div className="standard-card-header-title" > 
                                                        {result.title}
                                                        <table>
                                                            <tr>
                                                                <div className="foot-text flex flex-row standard-card-footer"> 
                                                                  <td>  <div className="data-align">  {result.sitename} </div> </td>
                                                                   <td>  <div className="data-align"> {result.pubDate} </div> </td>
                                                                </div>
                                                            </tr>
                                                        </table>

                                                </div>
                                            </td>
                                            <td>
                                                
                                            </td>
                                        </tr>

                                    </table>

                                </a>     
                     ))}
                </div>           
                </Container>
          </div>
        );
      }

}

export default CardDisplay