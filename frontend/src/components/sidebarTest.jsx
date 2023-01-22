import React from "react";

const coursedata = ["CPSC 110", "CPSC 121", "MATH 100", "MATH 101", "EOSC 114", "CHEM 121", "WRDS 150B", "CPSC 210", "DSCI 100", "SCIE 113"]

const checkdata = ["CPSC 110", "CPSC 121", "EOSC 114"]



export default function Testing() {
    
    function yayItWorks() {
        return <h6> working </h6>
    }

    function displayError() {
        return <h6> u suck </h6>
    }

    function presentData() {
        for (const c in checkdata) {
            if ((coursedata.includes(c)) === true) {
                continue
            } else {
                displayError()
            }
            yayItWorks()

        }
    }
    presentData();

}