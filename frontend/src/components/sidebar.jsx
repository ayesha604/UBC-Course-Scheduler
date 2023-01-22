import React , {useState, useEffect} from 'react';
import Button from 'react-bootstrap/Button';
import { AiOutlinePlus ,AiOutlineMinus } from "react-icons/ai";
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Alert from 'react-bootstrap/Alert';
import Container from 'react-bootstrap/Container';
import './Sidebar.scss'
import Stack from 'react-bootstrap/Stack';


const coursedata = ["CPSC 110", "CPSC 121", "MATH 100", "MATH 101", "EOSC 114", "CHEM 121", "WRDS 150B", "CPSC 210", "DSCI 100", "SCIE 113"]


export default function Sidebar({ handleSubmit }) {

    const [courseList, setCourseList] = useState([
        ""
    ]);
    const [invalidCourseList, setInvalidCourseList] = useState([
        ""
    ]);
    const [courseListError, setCourseListError] = useState(false) 

    console.log(courseList);


    function addCourse() {
        setCourseList([...courseList,  "" ]);
    }


    function checkCourseValidity(courseList) {

        let tmpInvalidCourseList = []
        setCourseListError(false)

        for (const c in courseList) {
            if ((coursedata.includes(courseList[c])) === false) {
                tmpInvalidCourseList.push(courseList[c]);
                setCourseListError(true)
                
            }
        }
        setInvalidCourseList(tmpInvalidCourseList)
    }     
     

    function removeCourse(index) {
        const list = [...courseList];
        list.splice(index, 1);
        setCourseList(list)
    }

    const handleCourseChange = (e, index) => {
        const {value} = e.target
        console.log(e);
        const list = [...courseList];
        list[index] = value;
        setCourseList(list);
    }

    const sendCourses = () => {
        if (checkCourseValidity(courseList)) {
            handleSubmit(courseList, 1)
        } else {
        }
    }

    function simulateNetworkRequest() {
        return new Promise((resolve) => setTimeout(resolve, 2000));
      }

    function loadingButton() {
        const [isLoading, setLoading] = useState(false);

        useEffect(() => {
        if (isLoading) {
            simulateNetworkRequest().then(() => {
              setLoading(false);
            });
          }
        }, [isLoading]);
      
        const handleClick = () => setLoading(true);
    }


    return (  
        <Container fluid>

            <Stack gap={3}>
                <div className="center">
                    <h6 class="fw-bold" style={{ color: "black"}}>Enter your courses:</h6>

                
                    {courseList.map((singleCourse, index) => (
                        <div key = {index}>
                                <InputGroup className="mb-3">
                                    <Form.Control
                                    placeholder="e.g. CPSC 110"
                                    aria-label="Course-username"
                                    aria-describedby="basic-addon2"
                                    
                                    value={courseList[index]}
                                    onChange = {(e) => handleCourseChange(e, index)}
                                    
                                    />
                                    
                                    
                                    <Button onClick={() => removeCourse(index)} variant='danger' id="button-addon2">
                                        <AiOutlineMinus style={{color: "white"}}>minus</AiOutlineMinus>
                                    </Button>

                            
                            </InputGroup>
                    </div>
                    ))}               

                    <div>
                        <Button onClick={() => addCourse()} variant="success">
                            <AiOutlinePlus style={{ color: "white"}}
                            variant='success'>plus</AiOutlinePlus>
                        </Button>
                    </div>      

                    <div style={{marginTop: "1em"}}>
                        <Button onClick={() => {sendCourses()}}
                        variant="primary">Submit</Button>   
                    </div> 

                    {courseListError &&
                        <div>
                            <Alert key={"danger"} variant={"danger"}>
                            <h6>The following courses are invalid: </h6> 
                            <div>
                            { invalidCourseList.map((c) => {
                                return (
                                    <>
                                    {c}
                                    </>
                                )
                            })} 
                            </div> 
                            </Alert>
                                                                
                        </div>   
                    }
                </div>
            

            </Stack>

        </Container>
    )
    
    

}
