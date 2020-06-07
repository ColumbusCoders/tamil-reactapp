import React from 'react'
import {Nav,Navbar,Form,FormControl,Button,NavDropdown} from 'react-bootstrap'
import {Container,Col,Row,Card,CardDeck,CardColumns,Accordion} from 'react-bootstrap';


class CardDisplay extends React.Component{

    render() {
        return (
            <div widh="%100" className="flex-grid-item" >
                <CardColumns>
                {this.props.feedResults.map(result => (
                        <Card  className="card-border">
                        <table>
                            <tr>
                                <td>                        
                                     <Card.Img className="images"  src={result.imagelink} />  
                                 </td>
                                 <td>  
                                    <a  href={result.link} >                    
                                    <Card.Body>
                                        <Card.Text className="standard-card-header-title">
                                            {result.title}
                                        </Card.Text>
                                    </Card.Body>     
                                    </a>     
                                </td>
                            </tr>
                            <tr >
                                <td>
                                </td>
                                <td className="text-align-center">
                                    <small >{result.sitename} | {result.pubDate} </small>
                                </td>

                            </tr>


                        </table>

                        </Card>
                     ))}
                </CardColumns>
          </div>
        );
      }

}

export default CardDisplay