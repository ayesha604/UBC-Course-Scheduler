export async function sendCourses(courses) {
    let response = await fetch('http://localhost:5000/schedule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "courses": courses,
            "term": 2
        })
    })
    return (await response.json())
}