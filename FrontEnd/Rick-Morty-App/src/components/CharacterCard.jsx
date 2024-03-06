import {Card, CardBody, CardImg, CardTitle, Col} from "react-bootstrap"


function CharacterCard () {
    return (
        <>
        <Col>
           <Card style={{ width: '18rem', height: '45rem'}}>
            <CardImg/>
            <CardBody>
                <CardTitle>Character</CardTitle>
            </CardBody>
           </Card>
        </Col>
        </>
        


    )
}

export default CharacterCard