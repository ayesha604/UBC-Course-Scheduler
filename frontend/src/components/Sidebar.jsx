import React , {useState, useEffect} from 'react';
import Button from 'react-bootstrap/Button';
import { AiOutlinePlus ,AiOutlineMinus } from "react-icons/ai";
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Alert from 'react-bootstrap/Alert';
import Container from 'react-bootstrap/Container';
import './Sidebar.scss'
import Stack from 'react-bootstrap/Stack';


//const coursedata = ["CPSC 110", "CPSC 121", "MATH 100", "MATH 101", "EOSC 114", "CHEM 121", "WRDS 150B", "CPSC 210", "DSCI 100", "SCIE 113"]


export default function Sidebar({ handleSubmit, courseData }) {

    const [courseList, setCourseList] = useState([
        ""
    ]);
    const [invalidCourseList, setInvalidCourseList] = useState([
        ""
    ]);
    const [courseListError, setCourseListError] = useState(false) 
    const [selectedTerm, setSelectedTerm] = useState();
    const [selectionError, setSelectionError] = useState(false)

    function addCourse() {
        setCourseList([...courseList,  "" ]);
    }


    function checkCourseValidity() {

        let tmpInvalidCourseList = []
        setCourseListError(false)

        for (const c in courseList) {
            if (selectedTerm && selectedTerm === 1) {
                if(courseData["Term 1"].includes(courseList[c]) === false) {
                    tmpInvalidCourseList.push(courseList[c]);
                    setCourseListError(true)
                }
            } else if (selectedTerm && selectedTerm === 2) {
                if (courseData["Term 2"].includes(courseList[c]) === false) {
                    tmpInvalidCourseList.push(courseList[c]);
                    setCourseListError(true)
                }
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
        const list = [...courseList];
        list[index] = value;
        setCourseList(list);
    }

    const sendCourses = () => {
        if(!selectedTerm) setSelectionError(true)
        else {
            setSelectionError(false)
            checkCourseValidity()
            if (!courseListError) {
                handleSubmit(courseList, selectedTerm)
            }
        }
    }

    return (  
        <Container fluid>
            <Stack gap={3}>
                <div className="center">
                    <h6 class="fw-bold" style={{ color: "black"}}>Enter your courses:</h6>

                    {courseList.map((singleCourse, index) => (
                        <InputGroup className="mb-3" key={index}>
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
                    ))}               

                    <div>
                        <Button onClick={() => addCourse()} variant="success">
                            <AiOutlinePlus style={{ color: "white"}}
                                        variant='success'>
                                plus
                            </AiOutlinePlus>
                        </Button>
                    </div>   

                    <div style={{paddingTop: "1em"}}>
                        <label htmlFor="term" style={{paddingRight: "0.5em"}}>Term: </label>
                        <Form.Check
                            inline
                            label={1}
                            name="term"
                            type="radio"
                            onChange={() => setSelectedTerm(1)}
                            checked={selectedTerm === 1}
                        />
                        <Form.Check
                            inline
                            label={2}
                            name="term"
                            type="radio"
                            onChange={() => setSelectedTerm(2)}
                            checked={selectedTerm === 2}
                        />
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
                                            <>{c}</>
                                        )
                                    })} 
                                </div> 
                            </Alert>                                   
                        </div>
                    }
                    {selectionError &&
                        <div>
                            <Alert key={"danger"} variant={"danger"}>
                                <h6>Please select a term.</h6>
                            </Alert>
                        </div>    
                    }
                </div>

            </Stack>

        </Container>
    )
    
    

}
