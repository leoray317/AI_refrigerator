$(function(){
    $('#fullpage').fullpage({
        paddingTop: '50px',
        anchors: ['homepage', 'video1', 'price', 'other','member'],
        sectionsColor: ['#f2f2f2', '#d3d3d3', '	#c0c0c0', '#ccddff','grey'],
        menu: '#myMenu',
        lockAnchors: false,
        navigation: true,
        navigationPosition: 'right',
        navigationTooltips: ['homepage', 'video1', 'price','other', 'member'],
        showActiveTooltip: false,
        slidesNavigation: false,
        slidesNavPosition: 'bottom',
    });
});
