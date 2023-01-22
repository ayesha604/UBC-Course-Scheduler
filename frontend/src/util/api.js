export async function sendCourses(courses, term) {
    let response = await fetch('http://localhost:5000/schedule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "courses": courses,
            "term": term
        })
    })
    return (await response.json())
}