// $('.hamburger-btn').on('click', (event) => {
//     $('.menu-hidden').addClass('visible');

// })

$('.chevron-right-first').on('click', (event) => {
    $('.first-slide').removeClass('open');
    $('.first-slide').removeClass('display');
    $('.second-slide').addClass('open');

})

$('.chevron-left-second').on('click', (event) => {
    $('.second-slide').removeClass('open');
    $('.second-slide').removeClass('display');
    $('.first-slide').addClass('open');

})

$('.chevron-right-second').on('click', (event) => {
    $('.second-slide').removeClass('open');
    $('.second-slide').removeClass('display');
    $('.third-slide').addClass('open');

})

$('.chevron-left-third').on('click', (event) => {
    $('.third-slide').removeClass('open');
    $('.third-slide').removeClass('display');
    $('.second-slide').addClass('open');

})

$('.chevron-right-third').on('click', (event) => {
    $('.third-slide').removeClass('open');
    $('.third-slide').removeClass('display');
    $('.fourth-slide').addClass('open');

})
$('.chevron-left-fourth').on('click', (event) => {
    $('.fourth-slide').removeClass('open');
    $('.fourth-slide').removeClass('display');
    $('.third-slide').addClass('open');

})
