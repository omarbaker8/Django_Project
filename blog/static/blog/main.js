$(document).ready(function() {
    let editor;

    if (typeof ClassicEditor !== 'undefined') {
        ClassicEditor.create(document.querySelector('#id_content'), {
            placeholder: 'Write your comment here!'

        }).then(newEditor => {
            editor = newEditor;
        }).catch(error => {
            console.error(error);
        });
    } else {
        console.error('ClassicEditor is not defined. Make sure CKEditor is properly loaded.');
    }

    // Add form submission handler
    $('form').submit(function(e) {
        if (editor) {
            const content = editor.getData();
            if (!content.trim()) {
                e.preventDefault();
                alert('Please enter a comment before submitting.');
            } else {
                $('#id_content').val(content);
            }
        }
    });
    //filp down counter
});

document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.card');
    
    cards.forEach((card) => {
        const endDateElement = card.querySelector('.list-group-item:nth-child(2)');
        const endDateString = endDateElement.textContent.split(': ')[1];
        const endDate = new Date(endDateString);
        const flipdownElement = card.querySelector('.flipdown');
        const flipdownContainer = card.querySelector('.flipdown-container');
        let flipdown;

        const now = new Date();
        const timeLeft = endDate.getTime() - now.getTime();
        
        if (timeLeft > 0) {
            // Convert end date to Unix timestamp in seconds
            const endDateUnix = Math.floor(endDate.getTime() / 1000);

            // Set up FlipDown
            flipdown = new FlipDown(endDateUnix, flipdownElement.id, {
                theme: 'dark',
                headings: ['Days', 'Hours', 'Minutes'],
            })
            .start()
            .ifEnded(() => {
                console.log('The project has ended!');
                flipdownContainer.textContent = 'Project has ended';
            });

            // Remove the seconds element
            setTimeout(() => {
                const secondsElement = flipdownElement.querySelector('.rotor-group:last-child');
                if (secondsElement) {
                    secondsElement.remove();
                }
            }, 50);

            flipdownContainer.style.display = 'block';
        } else {
            flipdownContainer.textContent = 'Project has ended';
            flipdownContainer.style.display = 'block';
        }
    });
});